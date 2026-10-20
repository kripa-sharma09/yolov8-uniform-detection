import argparse
from ultralytics import YOLO


def main():
    parser = argparse.ArgumentParser(
        description="Detect proper and improper uniforms in an image."
    )

    parser.add_argument(
        "--source",
        required=True,
        help="Path to the input image"
    )

    args = parser.parse_args()

    # Load the trained YOLOv8 model
    model = YOLO("weights/best.pt")

    # Run prediction and save the annotated image
    model.predict(
        source=args.source,
        save=True
    )

    print("Prediction completed!")


if __name__ == "__main__":
    main()