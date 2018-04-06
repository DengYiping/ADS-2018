object Timer {

  /*
  Generic timer for scala code block
   */
  def printsNano[R](codeBlock: => R): R = {
    //measure the time
    val t0 = System.nanoTime()
    //execute the code block
    val result = codeBlock //call by name
    val t1 = System.nanoTime()
    println(s"Elapsed time: ${t1 - t0} ms")
    result
  }

  def printsMillo[R](codeBlock: => R): R = {
    //measure the time
    val t0 = System.currentTimeMillis()
    //execute the code block
    val result = codeBlock //call by name
    val t1 = System.currentTimeMillis()
    println(s"Elapsed time: ${t1 - t0} ms")
    result
  }

  /*
  timer that returns
   */
  def mkNanoTuple[R](codeBlock: => R): (Long, R) = {
    //measure time
    val t0 = System.nanoTime()

    //call by name
    val result = codeBlock

    val t1 = System.nanoTime()
    (t1 - t0, result)
  }

  def mkMilloTuple[R](codeBlock: => R): (Long, R) = {
    //measure time
    val t0 = System.currentTimeMillis()

    //call by name
    val result = codeBlock

    val t1 = System.currentTimeMillis()
    (t1 - t0, result)
  }

}