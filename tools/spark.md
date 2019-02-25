# Spark


#### Transpose a rowMatrix
* Initialize a rowMatrix (requires RDD[Vector])
    ```scala
    val data = sc.parallelize(Array.fill(1000) {
      Vectors.dense(Array.fill(10000) {scala.util.Random.nextDouble})
    })
    val dMatrix = new RowMatrix(data)
    ```
* Transpose
    ```scala
    val transposedMatrix = dMatrix.rows.zipWithIndex.map { case (rowVec, rowIdx) =>
        rowVec.toArray.zipWithIndex.map { case (value, colIdx) => (colIdx.toLong, (rowIdx, value))}
    } // transpose a row, return triplet of col idx
      .flatMap(x => x)
      .groupByKey()
      .sortByKey().map(_._2) // sort row and remove indexes
      .map { r =>       // restore order
        val rArray = new Array[Double](r.size)
        r.foreach { case (idx, value) =>
            rArray(idx.toInt) = value
        }
        Vectors.dense(rArray)
      }
    ```
