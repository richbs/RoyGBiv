# RoyGBiv

This python module is intended to provide a set of image analysis tools. This is very much a work in progress...

_by Giv Parvaneh_

## Usage

	>>> from roygbiv import *
	>>> roy = Roygbiv('test.png')
	>>> roy.get_average_hex()
	'#468489'
	>>> roy.get_average_rgb()
	(70, 132, 137)