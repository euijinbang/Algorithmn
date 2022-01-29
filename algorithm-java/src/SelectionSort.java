public class SelectionSort {

    void selectionSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n; i++) {

            int min_idx = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[min_idx] > arr[j]) {
                    min_idx = j;
                }
            }

            int tmp = arr[i];
            arr[i] = arr[min_idx];
            arr[min_idx] = tmp;
        }
    }

    void printArray(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n; i++)
            System.out.println(arr[i] + " ");
        System.out.println();
    }

    public static void main(String[] args) {
        SelectionSort selectionSort = new SelectionSort();
        int[] arr = {12, 11, 13, 5, 6};
        selectionSort.selectionSort(arr);
        System.out.println("Sorted array");
        selectionSort.printArray(arr);
    }
}
