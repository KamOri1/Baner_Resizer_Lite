import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import customtkinter as ctk

from ui.ui_managers.slider_widgets import Widget


class FrameViewer(ctk.CTkFrame):
    def __init__(self, master, keyframes, close_callback, banner_catalog_name,close):
        super().__init__(master)
        self.keyframes_data = keyframes
        self.banner_catalog_name = banner_catalog_name
        self.current_frame_index: int = 0
        self.fig = None
        self.ax = None
        self.l = None
        self.close = close
        self.close_callback = close_callback

        self.create_widgets()
        self.create_slider_frame()

    def create_widgets(self) -> None:
        widget: Widget = Widget(master=self, accept=self.close_callback, close=self.close_frame, left_arrow=self.left_arrow, right_arrow=self.right_arrow)
        widget.show_widgets()
        widget.pack(side=ctk.BOTTOM, padx=0, pady=0)
        widget.configure(fg_color='#333333')

    def create_slider_frame(self) -> None:
        width_px: int = 950
        height_px: int = 400
        dpi: int = 100
        width_cal: int | float = (width_px + 20) / dpi
        height_cal: int | float = (height_px + 100) / dpi

        self.fig, self.ax = plt.subplots(figsize=(width_cal, height_cal), dpi=dpi, facecolor='#333333')
        plt.subplots_adjust(left=0.01, right=0.99, top=0.85, bottom=0.15)
        self.ax.set(xticks=[], yticks=[], facecolor="#333333")

        frame_video_index, frame_image = self.keyframes_data[self.current_frame_index]
        frame_index_counter: int = 1 if self.current_frame_index == 0 else self.current_frame_index + 1
        self.l = self.ax.imshow(frame_image, aspect='auto')
        self.fig.suptitle(f"{chr(0x2623)} {self.banner_catalog_name} {chr(0x2623)}", fontsize=18, color="#C0C0C0", y=1)
        self.subtitle = self.fig.text(0.5, 0.08,
                                      f'Frame #{frame_index_counter}',
                                      ha='center', va='top',
                                      fontsize=12, color="#ffffff")

        canvas = FigureCanvasTkAgg(self.fig, master=self)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(side='right', fill='both', expand=True, padx=(0, 0), pady=20)
        self.fig.canvas.mpl_connect('key_press_event', self.on_key_press)

    def update_image(self, index) -> None:
        if not self.keyframes_data:
            return

        self.current_frame_index: int = index
        frame_video_index, frame_image = self.keyframes_data[self.current_frame_index]
        frame_index_counter = 1 if self.current_frame_index == 0 else self.current_frame_index + 1
        self.l.set_data(frame_image)
        self.subtitle.set_text(f'Frame #{frame_index_counter}')
        self.fig.canvas.draw_idle()

    def right_arrow(self) -> None:
        if self.current_frame_index < len(self.keyframes_data) - 1:
            self.update_image(self.current_frame_index + 1)

    def left_arrow(self) -> None:
        if self.current_frame_index > 0:
            self.update_image(self.current_frame_index - 1)

    def on_key_press(self, event) -> None:
        if not self.keyframes_data:
            return
        if event.key == 'right':
            self.right_arrow()
        elif event.key == 'left':
            self.left_arrow()
        elif event.key == 'enter':
            self.close_callback()

    def chosen_frame(self) -> int:
        return self.current_frame_index

    def close_frame(self) -> None:
        self.close()

