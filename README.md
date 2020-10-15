# RANSAC-Algorithm

The goal of this task is to fit a line to a given set of points using RANSAC algorithm, and output
the names of inlier points and outlier points for the line. Specifically, there are in total 8 points,
and we need to find a line to best fit these points. After finding this line, we can use the
distance threshold t, to determine which points are inliers and which points are outliers. That is, a
point is inlier if the perpendicular distance of this point to the fit line is smaller than the
threshold t; otherwise, it belongs to outliers. The two initial points were recorded for
each iteration, such that you will not start from this two points in next iteration. The maximum
iterations it took was k = 100, and the program was finished within 1 minute.
