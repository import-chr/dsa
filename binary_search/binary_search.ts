const binary_search = ( arr: number[], value: number ): number => {
    let low: number = 0;
    let high: number = arr.length - 1;

    while( low <= high ) {
        let mid: number = Math.trunc((low + high) / 2);

        if( arr[mid] == value ) {
            return mid;
        } else if( arr[mid] > value ) {
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    return -1;
}