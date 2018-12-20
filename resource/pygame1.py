import pygame, sys
"""Line 1 is a simple import statement that imports the pygame and sys modules so that our program can use the functions in them. All of the Pygame functions dealing with graphics, sound, and other features that Pygame provides are in the pygame module. Note that when you import the pygame module you automatically import all the modules that are in the pygame module as well, such as pygame.images and pygame.mixer.music . There’s no need to import these modules-inside-modules with additional import statements."""
from pygame.locals import *
"""Line 3 is also an import statement. However, instead of the import modulename format, it uses the from modulename import * format. Normally if you want to call a function that is in a module, you must use the modulename.functionname() format after importing the module. However, with from modulename import * , you can skip the modulename. portion and simply use functionname() (just like Python’s built-in functions). The reason we use this form of import statement for pygame.locals is because pygame.locals contains several constant variables that are easy to identify as being in the pygame.locals module without pygame.locals. in front of them. For all other modules, you generally want to use the regular import modulename format. (There is more information about why you want to do this at http://invpy.com/namespaces.)"""
pygame.init()
"""Line 5 is the pygame.init() function call, which always needs to be called after importing the pygame module and before calling any other Pygame function. You don’t need to know what this function does, you just need to know that it needs to be called first in order for many Pygame functions to work. If you ever see an error message like pygame.error: font not initialized , check to see if you forgot to call pygame.init() at the start of your program."""
DISPLAYSURF = pygame.display.set_mode((400, 300))
"""Line 7 is a call to the pygame.display.set_mode() function, which returns the pygame.Surface object for the window. (Surface objects are described later in this chapter.) Notice that we pass a tuple value of two integers to the function: (400, 300) . This tuple tells the set_mode() function how wide and how high to make the window in pixels. (400, 300) will make a window with a width of 400 pixels and height of 300 pixels."""
pygame.display.set_caption('Hello World!')
while True: # main game loop
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()