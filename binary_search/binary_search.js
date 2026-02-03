function binary_search(arr, val) {
    let low = 0;
    let high = arr.length - 1;

    while(low <= high) {
        let mid = Math.trunc((low + high) / 2);

        if(arr[mid] == val) {
            return mid;
        } else if(arr[mid] > val) {
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    return -1;
}