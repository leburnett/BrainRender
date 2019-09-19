""" ------------------------------------------------------------------------------------------------------------------------------------------- """
        # WHOLE SCENE RENDERING OPTIONS
""" ------------------------------------------------------------------------------------------------------------------------------------------- """
VERBOSE = False                  # if True print useful messages during use
DISPLAY_INSET = True            # display a small version of the brain to show the orientation, 
                                # useful when the overall brian is not displayed (DISPLAY_ROOT). inset is crated at render time
DISPLAY_ROOT = True             # display the overall shape of the brain



""" ------------------------------------------------------------------------------------------------------------------------------------------- """
        # BRAIN REGIONS RENDERING OPTIONS
""" ------------------------------------------------------------------------------------------------------------------------------------------- """
DEFAULT_VIP_REGIONS = []        # list of acronyms of regions that must have different colors by default
DEFAULT_VIP_COLOR = [.8, .2, .2]  # default color of VIP regions

ROOT_COLOR = [.8, .8, .8]       # color of the overall brain model's actor
ROOT_ALPHA = .3                 # transparency of the overall brain model's actor'

DEFAULT_STRUCTURE_COLOR = [.8, .8, .8]  
DEFAULT_STRUCTURE_ALPHA = 0.25

""" ------------------------------------------------------------------------------------------------------------------------------------------- """
        # TRACTOGRAPHY & INJECTION RENDERING OPTIONS
""" ------------------------------------------------------------------------------------------------------------------------------------------- """
INJECTION_VOLUME_SIZE = 150    # injection locations are represented as spheres whose radius is injection-volume*INJECTION_VOLUME_SIZE
TRACTO_RADIUS = 20             # radius of tubes used to represent tracts
TRACTO_ALPHA = 1               # transparency of tracts
TRACTO_RES = 12                # resolution of tubes used to represent tracts
TRACT_DEFAULT_COLOR = "r"      # default color of tractography tubes
INJECTION_DEFAULT_COLOR = "g"  # default color for experiments injection sites

""" ------------------------------------------------------------------------------------------------------------------------------------------- """
        # MOUSE LIGHT NEURONS RENDERING VARIABLES
""" ------------------------------------------------------------------------------------------------------------------------------------------- """
DEFAULT_NEURITE_RADIUS = 10     # radius of dendrites, axons...
SOMA_RADIUS = 50                # radius of the soma sphere
NEURON_RESOLUTION = 24          # resolution of actors used to render the neuron, values of 12,24 are fine
NEURON_ALPHA = 1                # transparency of the neurons actors


""" ------------------------------------------------------------------------------------------------------------------------------------------- """
        # OTHER RENDERED VARIABLES
""" ------------------------------------------------------------------------------------------------------------------------------------------- """
SHADER_STYLE = "glossy"         # affects the look of rendered brain regions, valeus can be: [metallic, plastic, shiny, glossy] and can be changed in interactive mode
DECIMATE_NEURONS = False
SMOOTH_NEURONS = True


""" ------------------------------------------------------------------------------------------------------------------------------------------- """
        # DEBUG VARIABLES
""" ------------------------------------------------------------------------------------------------------------------------------------------- """
NEURONS_FILE = "D:\\Dropbox (UCL - SWC)\\Rotation_vte\\analysis_metadata\\anatomy\\Mouse Light\\neurons_in_PAG.json"





""" ------------------------------------------------------------------------------------------------------------------------------------------- """
        # CONSTANTS, SHOULD NOT BE CHANGED
""" ------------------------------------------------------------------------------------------------------------------------------------------- """
INTERACTIVE_MSG = """
 ==========================================================
| Press: i     print info about selected object            |
|        m     minimise opacity of selected mesh           |
|        .,    reduce/increase opacity                     |
|        /     maximize opacity                            |
|        w/s   toggle wireframe/solid style                |
|        p/P   change point size of vertices               |
|        l     toggle edges line visibility                |
|        x     toggle mesh visibility                      |
|        X     invoke a cutter widget tool                 |
|        1-3   change mesh color                           |
|        4     use scalars as colors, if present           |
|        5     change background color                     |
|        0-9   (on keypad) change axes style               |
|        k     cycle available lighting styles             |
|        K     cycle available shading styles              |
|        o/O   add/remove light to scene and rotate it     |
|        n     show surface mesh normals                   |
|        a     toggle interaction to Actor Mode            |
|        j     toggle interaction to Joystick Mode         |
|        r     reset camera position                       |
|        C     print current camera info                   |
|        S     save a screenshot                           |
|        E     export rendering window to numpy file       |
|        q     return control to python script             |
|        Esc   close the rendering window and continue     |
|        F1    abort execution and exit python kernel      |
| Mouse: Left-click    rotate scene / pick actors          |
|        Middle-click  pan scene                           |
|        Right-click   zoom scene in or out                |
|        Cntrl-click   rotate scene perpendicularly        |
|----------------------------------------------------------|
| Check out documentation at:  https://vtkplotter.embl.es  |
 ==========================================================
    """