""" Testing 

"""

import numpy as np

from nose.tools import assert_true, assert_false, \
     assert_equal, assert_raises

from numpy.testing import assert_array_equal, assert_array_almost_equal
import numpy.testing as npt

try:    
    from dipy.io.dpy import Dpy
    no_pytables = False    
except ImportError:
    no_pytables = True
    
try:    
    from dipy.viz import fvtk
    no_vtk = False
except ImportError:
    no_vtk = True

@npt.dec.skipif(no_vtk)
def test_fvtk_functions():
    
    # Create a renderer
    r=fvtk.ren()    
    
    # Create 2 lines with 2 different colors
    lines=[np.random.rand(10,3),np.random.rand(20,3)]    
    colors=np.random.rand(2,3)
    c=fvtk.line(lines,colors)    
    fvtk.add(r,c)    

    # Create a volume and return a volumetric actor using volumetric rendering        
    vol=100*np.random.rand(100,100,100)
    vol=vol.astype('uint8')    
    r = fvtk.ren()
    v = fvtk.volume(vol)
    fvtk.add(r,v)
    
    # Remove all objects
    fvtk.rm_all(r)
    
    # Put some text    
    l=fvtk.label(r,text='Yes Men')
    fvtk.add(r,l)

    # Show everything
    #fvtk.show(r)

    