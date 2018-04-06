import scala.annotation.tailrec

object MergeSortVariant {
  /*
  Generic merge function:
  Input: two already sorted list
  Output: merged and sorted list
   */
  def merge[T](xs: List[T], ys: List[T])( implicit ord: Ordering[T]): List[T] = {
    /*
    A tail recursive version
     */
    @tailrec
    def helper(`xs`: List[T], `ys`: List[T], aggr: List[T]): List[T] = (`xs`, `ys`) match {
      case (Nil, l2) =>
        aggr.reverse ::: l2
      case (l1, Nil) =>
        aggr.reverse ::: l1
      case (xsHead :: xsTail, ysHead :: ysTail) =>
        if(ord.lt(xsHead, ysHead))
          helper(xsTail, ysHead :: ysTail, xsHead :: aggr)
        else
          helper(xsHead :: xsTail, ysTail, ysHead :: aggr)
    }
    helper(xs, ys, Nil)
  }

  def mergeSortVariant[T](xs: List[T], insertion_depth: Int)( implicit ord: Ordering[T]): List[T] = {
    val len = xs.length
    if(len <= insertion_depth)
      insertionSort(xs)
    else {
      val (split1, split2) = xs.splitAt(len / 2)
      merge(mergeSortVariant(split1, insertion_depth), mergeSortVariant(split2, insertion_depth))
    }
  }

  /*
  Insert a element into a sorted list
   */
  def insert[T](x: T, xs: List[T])(implicit ord: Ordering[T]): List[T] = {
    /*
    Make it tail recursive so that it does not overflow the stack
     */
    @tailrec
    def helper(x: T, xs: List[T], aggr: List[T]): List[T] = xs match {
      case Nil =>
        (x :: aggr).reverse
      case y :: ys if ord.lt(x, y) =>
        aggr.reverse ::: (x :: y :: ys)
      case y :: ys =>
        helper(x, ys, y :: aggr)
    }
    helper(x, xs, Nil)
  }
  /*
  Implementation of insertion sort
   */
  def insertionSort[T](xs: List[T])(implicit ord: Ordering[T]): List[T] = {
    /*
    Make it tail recursive so that compiler to optimize
     */
    @tailrec
    def helper(xs: List[T], aggr: List[T]): List[T] = xs match {
      case Nil => aggr
      case xsHead :: xsTail => helper(xsTail, insert(xsHead, aggr))
    }
    helper(xs, Nil)
  }
  def generateRandom(n: Int): List[Int] = {
    val r = new scala.util.Random
    1 to n map { _ => r.nextInt() } toList
  }
  def generateWorst(n: Int) = generateRandom(n).sorted
  def generateBest(n: Int) = generateWorst(n).reverse

  def generateData(n:Int, timer: Int => Long): String = {
    val innerdata = (1 to n) map {_ * 10000} map { i => (i, (timer(i) + timer(i) + timer(i) ) / 3)} mkString ", "
    s"[$innerdata]"
  }
  def kToTime(k: Int, data: List[Int]):Long = {
    Timer.justTime(mergeSortVariant(data, k))
  }

  def main(args: Array[String]):Unit = {
    println("# Generate Plot data")

    val kVal = 20
    println("# Best case")
    println("bestPlot = " + generateData(20, {i:Int => kToTime(kVal, generateBest(i))}))

    println("# Worst case")
    println("worstPlot = " + generateData(20, {i:Int => kToTime(kVal, generateWorst(i))}))

    println("# Average case")
    println("avgPlot = " + generateData(20, {i:Int => kToTime(kVal, generateRandom(i))}))
  }
}
