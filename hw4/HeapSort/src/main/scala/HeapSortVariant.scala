object HeapSortVariant {
  import HeapSort._

  def moveBottom[T](a: Array[T], size: Int): Unit = {
    if(size <= 1)
      return
    val top = a(0)
    //move the array
    System.arraycopy(a, 1, a, 0, size - 1)
    a(size - 1) = top
  }
  def recoverBottom[T](a: Array[T], size: Int): Unit  = {
    if(size <= 1)
      return
    //recover the array
    val top = a(size - 1)
    System.arraycopy(a, 0, a, 1, size - 1)
    a(0) = top
  }

  def checkHeap[T](a: Array[T], parent: Int, size: Int)(implicit ord: Ordering[T]): Boolean = {
    val left = indexLeft(parent)
    val right = indexRight(parent)

    var largest = -1
    largest = if(left < size && ord.gt(a(left), a(parent))) left else parent
    largest = if(right < size && ord.gt(a(right), a(largest))) right else largest

    if(left < size && right < size)
      largest == parent && checkHeap(a, left, size) && checkHeap(a, right, size)
    else if (left < size)
      largest == parent && checkHeap(a, left, size)
    else if (right < size)
      largest == parent && checkHeap(a, right, size)
    else
      true
  }

  def tryBottom[T](a: Array[T],  size: Int)(implicit ord: Ordering[T]):Boolean = {
    //try to move to the bottom
    if(size <= 1)
      return true

    moveBottom(a, size)


    /*
    val parent = indexParent(size - 1)
    val left = indexLeft(parent)
    val right = indexRight(parent)

    var largest = -1
    largest = if(left < size && ord.gt(a(left), a(parent))) left else parent
    largest = if(right < size && ord.gt(a(right), a(largest))) right else largest

*/
    if(size == 2 && checkHeap(a, 0, 2))
      true
    //need to make sure the top part is working and the ending leaf is working
    if(checkHeap(a, indexParent(size - 1), size) && checkHeap(a, 0, 3))
      true
    else {
      recoverBottom(a, size)
      false
    }
  }
  def heapSortVariant[T](a: Array[T])(implicit ord: Ordering[T]):Unit = {
    maxHeapBuild(a, a.length)
    for(i <- a.indices.reverse){
      //in a reverse order sort it
      swap(a, 0, i) //put the last one at the back
      if(!tryBottom(a, i)) maxHeapify(a, 0, i) //only heapify when it is not right
    }
  }

  def genArray(n: Int):Array[Int] = {
    val r = new scala.util.Random
    1 to n map { _ => r.nextInt(100)} toArray
  }
  def dataGenerator[T](sort_algo:(Array[Int]) => Unit):String = {
    val input = (1 to 40) map { _ * 1000}
    //generate data set
    val result = input map {
      n =>
        val arr = genArray(n)
        (n, Timer.avergedJustTime(sort_algo(arr)))
    }

    "[" + result.mkString(",") + "]"
  }
  def main(args: Array[String]):Unit = {
    // the program that produces results
    println("normal = " + dataGenerator(heapSort[Int]))
    println("variant = " + dataGenerator(heapSortVariant[Int]))
  }
}
