import superannotate as sa

sa.create_project("Example Project 1", "example", "Vector")

sa.upload_images_from_folder_to_project("Example Project 1", "<path_to_my_images_folder>")