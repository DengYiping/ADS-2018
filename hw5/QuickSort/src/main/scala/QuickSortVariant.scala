object QuickSortVariant {
  def swap[T](arr: Array[T], i1: Int, i2: Int):Unit = {
    val tmp = arr(i1)
    arr(i1) = arr(i2)
    arr(i2) = tmp
  }

  def partition[T](arr: Array[T], first: Int, last: Int)(implicit ord: Ordering[T]):(Int, Int) = {
    //make a three way partition
    //return the index of first and second pivot
    //just don't do stupid thing with this three way partition

    if ((last - first) >= 3) {
      //choose first two as pivot
      if (ord.gt(arr(first), arr(first + 1))) {
        swap(arr, first, first + 1)
      }
      //put it at front and back
      swap(arr, first + 1, last)

      val p = arr(first)
      val q = arr(last)

      var l = first + 1
      var g = last - 1
      var k = l

      //maintain the loop invariant
      while (k <= g) {
        if (ord.lt(arr(k), p)) {
          //move the lower up, add one
          swap(arr, k, l)
          l = l + 1
        } else if (ord.gteq(arr(k), q)) {
          //move the bound for last partition in the right position
          while (ord.gt(arr(g), q) && k < g)
            g = g - 1

          swap(arr, k, g) //add one more
          g = g - 1

          if (ord.lt(arr(k), p)) {
            //if the new swapped can be move to even lower categories
            swap(arr, k, l)
            l = l + 1
          }
        }
        k = k + 1 //move the index
      }
      //fix the index
      l = l - 1
      g = g + 1

      //move the pivot in place
      swap(arr, first, l)
      swap(arr, last, g)

      //return the pivot
      (l, g)
    } else if (first == last - 1) {
      //two element partition
      if (ord.gt(arr(first), arr(last)))
        swap(arr, first, last)
      (first, last)
    } else if (first == last - 2) {
      //three element partition
      if (ord.gt(arr(first), arr(first + 1)))
        swap(arr, first, first + 1)
      if (ord.gt(arr(first + 1), arr(last)))
        swap(arr, first + 1, last)
      if (ord.gt(arr(first), arr(first + 1)))
        swap(arr, first, first + 1)
      (first, last)
    } else if(first == last){
      (first, first)
    } else {
      //should never happen
      throw new Exception
    }
  }



  def helper[T](arr: Array[T], first: Int, last: Int)(implicit ord: Ordering[T]):Unit = {
    //sorting from the first to the last, including the last

    if(first < last){
      val (p1, p2) = partition(arr, first, last)
      helper(arr, first, p1 - 1)
      helper(arr, p1 + 1, p2 - 1)
      helper(arr, p2 + 1, last)
    }
    //put this two pivot in the right order
  }

  def apply[T](arr: Array[T])(implicit ord: Ordering[T]):Unit = {
    // the main algorithm
    // just call the helper function
    helper(arr, 0, arr.length - 1)
  }

}
