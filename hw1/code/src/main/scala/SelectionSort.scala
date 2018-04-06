import javax.print.DocFlavor.BYTE_ARRAY

import scala.annotation.tailrec

object SelectionSort {


  /*
  Calculate the minimum
   */
  def indexOfMin[T](start: Int, arr: Array[T])(implicit odr: scala.math.Ordering[T]): Int = {
    var min_idx = start
    var i = start + 1
    while(i < arr.length){
      if(odr.lt(arr(i),arr(min_idx)))
        min_idx = i
      i = i + 1
    }
    min_idx
  }

  @inline
  def swap[T](i: Int, j:Int, arr: Array[T]): Unit = {
    val tmp = arr(i)
    arr(i) = arr(j)
    arr(j) = tmp
  }

  /*
  Implement selection sort algorithm
   */
  def selectionSort[T](arr: Array[T])(implicit odr: scala.math.Ordering[T]): Array[T] = {
    var unsortedIdx = 0;
    while(unsortedIdx < arr.length){
      swap(unsortedIdx, indexOfMin(unsortedIdx, arr), arr)
      unsortedIdx = unsortedIdx + 1
    }
    arr
  }

  /*
  Generate random list of integer
   */
  def generateRandomCase(n: Int): Array[Int] = {
    var r = new scala.util.Random
    (1 to n) map {_ => r.nextInt()} toArray
  }

  /*
  Simply sort the list
   */
  def generateBestCase(n: Int): Array[Int] = generateRandomCase(n).sorted
  /*
  Reverse the sorted list
   */
  def generateWorstCase(n: Int): Array[Int] = generateRandomCase(n).sortWith(_ >= _) //sort in reverse order


  /*
  Test case
   */
  def main(args: Array[String]): Unit = {
    val bestCases = 1 to 5 map {_ => generateBestCase(10000)} toList
    val worstCases = 1 to 5 map {_ => generateWorstCase(10000)} toList

    // HotSpot VM warm up
    // Since Java Virtual Machine implement JIT and HotSpot algorithm by default
    // warm up a function will lead to its JIT
    //(1 to 30).foreach(_ => selectionSort(generateWorstCase(1000)))


    // start calculation
   /*
    println("Worst case:")
    println(worstCases.head mkString " ")
    worstCases foreach {Timer printsMillo selectionSort[Int](_)}
    println("------")

    println("Best case: ")
    println(bestCases.head mkString " ")
    bestCases foreach {Timer printsMillo selectionSort[Int](_)}
    */
    // prepare dataset
    val datasetBest = (1 to 20).map(_ * 1000).map(i => (i, generateBestCase(i))).toList //force evaluation
    //run multiple times
    val tryTime = 5
    val resultBest = (1 to tryTime).map { i => datasetBest map {
      case (num: Int, arr: Array[Int]) => (num, Timer.mkMilloTuple(selectionSort(arr))._1)
    }}.reduce(_ zip _ map {
      t => (t._1._1, t._1._2 + t._2._2)
    }).map(t => (t._1, t._2 / tryTime))

    val datasetWorst = (1 to 20).map(_ * 1000).map(i => (i, generateWorstCase(i))).toList //force evaluation
    val resultWorst = (1 to tryTime).map { i => datasetBest map {
      case (num: Int, arr: Array[Int]) => (num, Timer.mkMilloTuple(selectionSort(arr))._1)
    }}.reduce(_ zip _ map {
      t => (t._1._1, t._1._2 + t._2._2)
    }).map(t => (t._1, t._2 / tryTime))

    val datasetAvg = (1 to 20).map(_ * 1000).map(i => (i, generateRandomCase(i))).toList //force evaluation
    val resultAvg = (1 to tryTime).map { i => datasetAvg map {
      case (num: Int, arr: Array[Int]) => (num, Timer.mkMilloTuple(selectionSort(arr))._1)
    }}.reduce(_ zip _ map {
      t => (t._1._1, t._1._2 + t._2._2)
    }).map(t => (t._1, t._2 / tryTime))
    //print the resulting tuples
    println("# Statistics for (d)")
    println("# Best case")
    println(resultBest)
    println("# Worst case")
    println(resultWorst)
    println("# Average case")
    println(resultAvg)
  }
}