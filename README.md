Short Write-up
Code Structure
The code is organized in a class MobiusStrip that:

Accepts strip parameters (radius, width, resolution).

Generates a 3D mesh using parametric equations.

Computes surface area using double numerical integration.

Computes edge length along the boundary of the strip.

Displays a 3D plot using matplotlib.

Surface Area Approximation
The surface area is computed numerically by:

Defining a function to calculate the local surface element using derivatives.

Evaluating this function over a grid of 
(
𝑢
,
𝑣
)
(u,v) values.

Applying Simpson’s Rule twice — once over v and then over u — to integrate over the surface.

Edge Length Calculation
The edge curve (v = ±w/2) is sampled as a parametric curve in 3D space, and the total edge length is approximated by:
Challenges Faced
Ensuring numerical stability in surface area approximation.

Properly aligning axis dimensions for Simpson integration.

Managing gradient precision in edge length computation.


