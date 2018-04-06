class TimesRepeat private (n: Int) {
  def timesRepeat[T](block: => T) = (1 to n) map {_ => block}
}
object TimesRepeat {
  implicit def toTimesRepeat(n:Int) = new TimesRepeat(n)
}
