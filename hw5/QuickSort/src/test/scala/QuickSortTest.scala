import org.scalatest.FlatSpec

class QuickSortTest extends FlatSpec {
  "A Partition algorithm" should "divide the array properly in all case" in {
    val arr = Array(2, 1)
    val (t1, t2) = QuickSortVariant.partition(arr, 0, 1)
    assert(arr(t1) < arr(t2))

    val arr1 = Array(2,1, -1, 3, 4, 0)
    val (t3, t4) = QuickSortVariant.partition(arr1, 0, arr1.length - 1)
    println(arr1.mkString(","))
    println(t3)
    println(t4)
    assert(t3 == 2)
    assert(t4 == 3)

    val r = scala.util.Random
    val rand_arr = (1 to 50).map{ _ => r.nextInt(100)}.toArray
    val (p1, p2) = QuickSortVariant.partition(rand_arr, 0, rand_arr.length - 1)

    val sub_arr1 = rand_arr.slice(0, p1)
    println(sub_arr1.mkString(" "))
    val sub_arr2 = rand_arr.slice(p1, p2)
    println(sub_arr2.mkString(" "))
    val sub_arr3 = rand_arr.slice(p2, rand_arr.length)
    println(sub_arr3.mkString(" "))

  }
  "A sorting algorithm" should "sort everything in place" in {
    val r = scala.util.Random
    val arr = (1 to 50) map { _ => r.nextInt(100)} toArray
    val arr1 = arr.clone().sorted //make a copy of the array and sort
    val arr2 = arr.clone()

    QuickSortVariant(arr)

    assert(arr.deep == arr1.deep)

    QuickSortVariantRandom(arr2)

    assert(arr2.deep == arr1.deep)
  }
}
