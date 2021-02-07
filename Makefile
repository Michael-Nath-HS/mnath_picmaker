make: picmaker.py
	python3 picmaker.py
	sips -s format png image.ppm --out image.png
clean:
	rm image.ppm
	rm image.png 