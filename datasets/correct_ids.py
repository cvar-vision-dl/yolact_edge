import json
import os
import argparse

def parse_args():

    parser = argparse.ArgumentParser(description="Correct the ids in the json file")
    parser.add_argument("--json_file", required=True, help="Path to the json file")
    parser.add_argument("--output_file", required=True, help="Path to the output file")
    args = parser.parse_args()
    print(args)
    return args

def get_all_ids(json_obj):
    ids = []
    for img_dict in json_obj["images"]:
        ids.append(img_dict["id"])

    return ids

def ids_to_int(json_obj):

    ids = get_all_ids(json_obj)
    for img_dict in json_obj["images"]:
        img_dict["id"] = ids.index(img_dict["id"])

    for ann_dict in json_obj["annotations"]:
        ann_dict["image_id"] = ids.index(ann_dict["image_id"])

    return json_obj

def segmentation_to_list_of_lists(json_obj):

    for ann_dict in json_obj["annotations"]:
        ann_dict["segmentation"] = [ann_dict["segmentation"]]        

    return json_obj

if __name__ == '__main__':

    args = parse_args()

    with open(args.json_file, "r") as f:
        json_obj = json.load(f)

    json_obj = ids_to_int(json_obj)
    json_obj = segmentation_to_list_of_lists(json_obj)

    with open(args.output_file, "w") as f:
        json.dump(json_obj, f, indent=4)

    print("Done")