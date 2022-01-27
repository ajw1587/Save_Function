def resize_aspect_ratio(img, final_h, final_w):
    height, width, channel = img.shape
    ratio = 0
    # height = 8914
    # width = 6457
    target_w_size = final_w
    target_h_size = final_h

    h_ratio = target_h_size / height
    target_h, target_w = int(height * h_ratio), int(width * h_ratio)
    diff = target_w_size - target_w
    if diff > 0:
        resized = cv2.resize(img, (target_w, target_h), interpolation=interpolation)
        pad_array = np.ones(shape=(target_h_size, diff, 3), dtype=np.uint8)
        # pad_array = np.full(shape=(target_h_size, diff, 3), 255)
        resized = np.append(resized, pad_array, axis=1)
        ratio = h_ratio
    else:
        w_ratio = target_w_size / width
        target_h, target_w = int(height * w_ratio), int(width * w_ratio)
        diff = target_h_size - target_h
        resized = cv2.resize(img, (target_w, target_h), interpolation=interpolation)
        pad_array = np.ones(shape=(diff, target_w_size, 3), dtype=np.uint8)
        resized = np.append(resized, pad_array, axis=0)
        ratio = w_ratio

    cv2.imshow('test', resized)
    cv2.waitKey(0)