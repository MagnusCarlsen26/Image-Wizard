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




def image_enhance(cv2_image, boundary_pts):
  
    # Iterate through each point inside the boundary and divide by 9
    for y in range(cv2_image.shape[0]):
        for x in range(cv2_image.shape[1]):
            if cv2.pointPolygonTest(boundary_pts, (x, y), False) >= 0:
                cv2_image[y, x] //= 9  # Divide each channel by 9
    
    return cv2_image


def darken(cv2_image, boundary_pts):
    cv2_image = cv2_image.copy()
    for y in range(cv2_image.shape[0]):
        for x in range(cv2_image.shape[1]):
            if cv2.pointPolygonTest(boundary_pts, (x, y), False) >= 0:
                cv2_image[y, x] -= 128  # Divide each channel by 9
    
    return cv2_image

def lower_contrast(cv2_image, boundary_pts):
    cv2_image = cv2_image.copy()
    for y in range(cv2_image.shape[0]):
        for x in range(cv2_image.shape[1]):
            if cv2.pointPolygonTest(boundary_pts, (x, y), False) >= 0:
                cv2_image[y, x] //= 2  # Divide each channel by 9
    
    return cv2_image

def non_linear_lower(cv2_image, boundary_pts):
    cv2_image = cv2_image.copy()
    for y in range(cv2_image.shape[0]):
        for x in range(cv2_image.shape[1]):
            if cv2.pointPolygonTest(boundary_pts, (x, y), False) >= 0:
                cv2_image[y, x] = ((cv2_image[y, x]/255)**(1/3))*255  # Divide each channel by 9
    
    return cv2_image

def invert(cv2_image, boundary_pts):
    cv2_image = cv2_image.copy()
    for y in range(cv2_image.shape[0]):
        for x in range(cv2_image.shape[1]):
            if cv2.pointPolygonTest(boundary_pts, (x, y), False) >= 0:
                cv2_image[y, x] = 255 - cv2_image[y, x] # Divide each channel by 9
    
    return cv2_image

def lighten(cv2_image, boundary_pts):
    cv2_image = cv2_image.copy()
    for y in range(cv2_image.shape[0]):
        for x in range(cv2_image.shape[1]):
            if cv2.pointPolygonTest(boundary_pts, (x, y), False) >= 0:
                cv2_image[y, x] *= 3  # Divide each channel by 9
    
    return cv2_image

def raise_contrast(cv2_image, boundary_pts):
    cv2_image = cv2_image.copy()
    for y in range(cv2_image.shape[0]):
        for x in range(cv2_image.shape[1]):
            if cv2.pointPolygonTest(boundary_pts, (x, y), False) >= 0:
                cv2_image[y, x] *= 2  # Divide each channel by 9
    
    return cv2_image

def non_linear_raise(cv2_image, boundary_pts):
    cv2_image = cv2_image.copy()
    for y in range(cv2_image.shape[0]):
        for x in range(cv2_image.shape[1]):
            if cv2.pointPolygonTest(boundary_pts, (x, y), False) >= 0:
                cv2_image[y, x] = ((cv2_image[y, x]/255)**(2))*255  # Divide each channel by 9
    
    return cv2_image