# vessel_simulator
A toolbox for vessel X-ray angiography images simulation.

```
@inproceedings{maccagnan2023toolbox,
  title={Toolbox for vessel X-ray angiography images simulation},
  author={Maccagnan, Gabriela Copetti and Schmith, Jean and Santos, Marcia and de Figueiredo, Rodrigo Marques},
  booktitle={Anais do XXIII Simp{\'o}sio Brasileiro de Computa{\c{c}}{\~a}o Aplicada {\`a} Sa{\'u}de},
  pages={59--70},
  year={2023},
  organization={SBC}
}
```

For more information refer to our [article](https://sol.sbc.org.br/index.php/sbcas/article/view/25277/25098).

## Requirements
- [Python](https://www.python.org/)
- [Matplotlib](https://matplotlib.org/)

## Content

```
├ dataset
  ├ aneurysm
  ├ normal
  ├ stenosis
├ VesselSimulator.py
├ vs_example.py
```

### dataset
This folder contains readily available images created with our algorithm, you are free to use them. In here you'll find synthetic images of healthy vessels (normal folder) and vessels with diseases (stenosis and aneurysm folders). 

### vs_example
In this file you'll find an assembly example for every vessel shape, as well as left and right coronary arteries models. The functions in here can either be used as they are, or used as basis for the construction of new functions.

### VesselSimulator
This file contains the functions that can be used to create vessel images. So far there are five functions for vessel shapes (Line, Second Degree, Sine, Bézier, End Vessel), one function for stenosis and aneurysm simulation and one for vessel thinning simulation.

## How to Use

To use the available models in [vs_example](https://github.com/jeanschmith/vessel_simulator/blob/main/vs_example.py):

1. Either clone this repository or download it 

2. Import package:
```bash
import vs_example as vse
```

3. Call any of the functions:

For single vessel images:
```bash
vse.line_generator()
vse.line_v2_generator()
vse.sec_degree_generator()
vse.sine_generator()
vse.bezier_generator()
vse.end_vessel_generator()
```

For left coronary images:
```bash
vse.lca_generator()
vse.lca_v2_generator()
```

For right coronary images:
```bash
vse.rca_generator()
vse.rca_v2_generator()
```

To create new functions using [VesselSimulator](https://github.com/jeanschmith/vessel_simulator/blob/main/VesselSimulator.py):

1. Either clone this repository or download it 

2. Import package:
```bash
import VesselSimulator as vs
```

3. Define an empty array for all vessel points: 
```bash
points = []
```

4. Define the following image and vessel parameters:
```bash
image_height
image_width
vessel_line_width
noise_grade
stenosis_grade
stenosis_length
stenosis_position
thinning_factor
```

Consider that ```stenosis_grade``` and ```thinning_factor``` go up until 1.0

5. Define your points:
```bash
point_a = (x_a, y_a)
point_b = (x_b, y_b)
point_c = (x_c, y_c)
...
```

6. Assemble the vessel image (the following example has two connected vessels, but you can define as many as you'd like):
```bash
C1 = vs.make_sine([point_a, point_b], amplitude, frequency) # calculates all the points for the vessel beginning on point_a and ending on point_b based on the type of curve
C1 = vs.make_normal(C1, vessel_line_width) # applies a width to the vessel
points_width.extend(C1)

C2 = vs.make_end_vessel([point_b, point_c], amplitude) # calculates the points for the next vessel beginning on point_b
C2 = vs.make_stenosis_aneurysm(C2, stenosis_position, stenosis_length, stenosis_grade, vessel_line_width, "stenosis") # applies a width to the vessel and also modifies it with an stenosis
C2 = vs.make_thinning(C2, thinning_factor) # modifies vessel width to make it tapered
points.extend(C2)

image = vs.draw_vessel_image(image_width, image_height, noise_grade, points) # puts together the vessels, background and image noise

plt.figure()
plt.imshow(image, cmap="gray")
plt.axis('off')
plt.show()
```

## Contribute
If you'd like to contribute or have a suggestion for improvement, let us know by filling an issue.
