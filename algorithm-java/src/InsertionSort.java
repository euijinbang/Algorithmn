public class InsertionSort {

    void insertionSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            int key = arr[i];
            int j = i - 1;

            while (j >= 0 && key < arr[j]) {
                arr[j + 1] = arr[j];
                j -= 1;
            }
            arr[j + 1] = key;
        }
    }

    void printArray(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n; i++)
            System.out.println(arr[i] + " ");
        System.out.println();
    }

    public static void main(String[] args) {
        InsertionSort insertionSort = new InsertionSort();
        int[] arr = {12, 11, 13, 5, 6};
        insertionSort.insertionSort(arr);
        System.out.println("Sorted array");
        insertionSort.printArray(arr);
    }
}
