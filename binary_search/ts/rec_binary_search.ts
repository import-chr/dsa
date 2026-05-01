const rec_binary_search = (arr: number[], low: number, high: number, val: number): number => {
    if( low > high ) return -1;

    let mid: number = Math.trunc((low + high) / 2);

    if( arr[mid] == val ) {
        return mid;
    } else if( arr[mid] > val ) {
        return rec_binary_search(arr, low, mid - 1, val);
    } else {
        return rec_binary_search(arr, mid + 1, high, val);
    }
}