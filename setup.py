from distutils.core import setup

setup(
	name='cypy',
	version='0.2.0',
	author='Cyrus Omar',
	author_email='cyrus.omar@gmail.com',
        packages=['cypy', 'cypy.np'],
	py_modules=['cypy', 'cypy.cg', 'cypy.astx', 'cypy.np', 'cypy.np.plotting'],
	url='http://github.com/cyrus-/cypy',
	license='MIT',
	description='Useful utilities for Python.',
	long_description="",
	install_requires=[]
)
