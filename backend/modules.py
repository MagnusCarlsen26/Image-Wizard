import cv2
import numpy as np


def back_black(image_old,boundary_pts):
    image = image_old.copy()
    filled_image = np.zeros_like(image)
    cv2.drawContours(filled_image , [boundary_pts], 0 , (0,255,0) , thickness=cv2.FILLED)
    return filled_image


def back_normal(image_old,boundary_pts):
    image = image_old.copy()
    
    cv2.drawContours(image , [boundary_pts], 0 , (0,255,0) , thickness=cv2.FILLED)
    return image


def back_white(image_old,boundary_pts):
    image = image_old.copy()
    filled_image = np.ones_like(image) * 255
    cv2.drawContours(filled_image , [boundary_pts], 0 , (0,0,255) , thickness=cv2.FILLED)
    return filled_image


def alpha_blending(image_old, boundary_pts, alpha):
    image = image_old.copy()
    filled_image = np.zeros_like(image, dtype=np.uint8)
    cv2.drawContours(filled_image, [boundary_pts], 0, (0, 255, 0), thickness=cv2.FILLED)
  
    output_image = cv2.addWeighted(image, 1, filled_image, alpha / 255, 0)
    return output_image

def transparent_bg(image_old, boundary_pts):
    image = image_old.copy()
    # Create a blank mask with the same dimensions as the original image
    mask = np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)

    # Draw the contour of the boundary filled with white color on the mask
    cv2.drawContours(mask, [boundary_pts], 0, (255), thickness=cv2.FILLED)
    mask = np.logical_not(mask)
    image[mask] = [0,255,0]
    return image



