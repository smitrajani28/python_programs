import pyheif
import os


def heic_to_jpg(input_path, output_path):
  """Converts a HEIC image to a JPG image.

  Args:
    input_path: The path to the input HEIC image.
    output_path: The path to the output JPG image.
  """

  with open(input_path, "rb") as f:
    heif_image = pyheif.read(f)

  jpg_image = heif_image.as_jpeg()

  with open(output_path, "wb") as f:
    f.write(jpg_image)

if __name__ == "__main__":
  list1 = os.listdir("files")
  os.chdir("files")
  for i in range(0,len(list1)):
    input_path = list1[i]
    output_path = i + ".jpg"
    heic_to_jpg(input_path, output_path)