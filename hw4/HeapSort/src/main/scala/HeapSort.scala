object HeapSort {
  def indexLeft(i: Int) = (2 * i) + 1 // zero indexed system
  def indexRight(i: Int) = indexLeft(i) + 1
  def indexParent(i: Int) = (i - 1) / 2

  def swap[T](a: Array[T], i: Int, j: Int): Unit = {
    //generic swap function for array
    val tmp = a(i)
    a(i) = a(j)
    a(j) = tmp
  }

  def maxHeapify[T](a: Array[T], i: Int, size: Int)(implicit ord: Ordering[T]): Unit = {
    //heapify at index i
    val idxLeft = indexLeft(i)
    val idxRight = indexRight(i)

    //find the largest in the small tree branch
    var largest = -1
    largest = if(idxLeft < size && ord.gt(a(idxLeft), a(i))) idxLeft else i
    largest = if(idxRight < size && ord.gt(a(idxRight), a(largest))) idxRight else largest
    if(largest != i){
      swap(a, i, largest)
      maxHeapify(a, largest, size)
      // let A[i] float down so that A[i] is always larger than its branches
    }
  }

  def maxHeapBuild[T](a: Array[T], size: Int)(implicit ord: Ordering[T]): Unit = {
    val half = size / 2
    for( i <- 0 to half){
      maxHeapify(a, half - i, size) //in a backward order
    }
  }

  def heapSort[T](a:Array[T])(implicit ord: Ordering[T]):Unit = {
    maxHeapBuild(a, a.length) //build a maxheap
    for(i <- (0 until a.length).reverse){
      //in a reverse order sort it
      swap(a, 0, i) //put the last one at the back
      maxHeapify(a, 0, i) //the size is changing
    }
  }
}
