from manim import *
import numpy as np
from scipy.integrate import solve_ivp


def lorenz(t, state, sigma=10, rho=28, beta=8 / 3):
    x, y, z = state
    return [sigma * (y - x), x * (rho - z) - y, x * y - beta * z]


class LorenzAttractor(ThreeDScene):
    def construct(self):
        # 1. Solve the Lorenz system
        t_span = (0, 40)
        t_eval = np.linspace(0, 40, 10000)
        sol = solve_ivp(lorenz, t_span, [1, 1, 1], t_eval=t_eval)

        x, y, z = sol.y

        # 2. Add a bounding 3D coordinate space to frame the chaos
        axes = ThreeDAxes(
            x_range=[-30, 30, 10],
            y_range=[-30, 30, 10],
            z_range=[0, 50, 10],
            x_length=6,
            y_length=6,
            z_length=5,
        )
        self.add(axes)

        # 3. Map raw math states onto the exact coordinate paths
        points = [axes.coords_to_point(x[i], y[i], z[i]) for i in range(len(t_eval))]

        # Set up 3D camera
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.15)

        # Draw with color gradient
        curves = VGroup()
        step = 100
        for i in range(0, len(points) - step, step):
            t = i / len(points)
            color = interpolate_color(BLUE, RED, t)
            segment = VMobject()
            segment.set_points_smoothly(points[i : i + step + 1])
            segment.set_stroke(color=color, width=1.5, opacity=0.8)
            curves.add(segment)

        # Execute render loop
        self.play(Create(curves), run_time=10, rate_func=linear)
        self.wait(5)
