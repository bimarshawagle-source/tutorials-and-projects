import cv2
import easyocr


def recognize_letters(image_path, min_confidence , save_annotated):
    
    # Initialize EasyOCR reader for English ('gpu=False' works on CPU; set to False as Gpu was not detected)
    reader = easyocr.Reader(["en"], gpu=False)

    # Read image with OpenCV to verify it loads properly
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Could not load image at: {image_path}")

    # Run OCR: returns list of (bounding_box, text, confidence)
    results = reader.readtext(image_path)

    print(f"Results for '{image_path}':\n" + "-" * 45)
    found_any = False

    for bbox, text, confidence in results:
        if confidence < min_confidence:
            continue

        found_any = True
        print(f"Detected: '{text}' | Confidence: {confidence:.2%}")

        if save_annotated:
            top_left = tuple(map(int, bbox[0]))
            bottom_right = tuple(map(int, bbox[2]))
            cv2.rectangle(image, top_left, bottom_right, (0, 200, 0), 2)
            label_pos = (top_left[0], max(top_left[1] - 10, 20))
            cv2.putText(
                image,
                f"{text} ({confidence:.2f})",
                label_pos,
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 150, 0),
                2,
            )

    if not found_any:
        print("No letters or text detected above the confidence threshold.")

    if save_annotated:
        output_path = "annotated_output.png"
        cv2.imwrite(output_path, image)
        print("-" * 45 + f"\nSaved annotated image to '{output_path}'")



sample_image = r"C:/Users/user/Documents/local_repo_1/week_0/ml_basic/A_ocrtest.png"  # this is the image path
recognize_letters(sample_image, min_confidence=0.05, save_annotated=True)