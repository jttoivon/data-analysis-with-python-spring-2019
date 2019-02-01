.. Data analysis with Python documentation master file, created by
   sphinx-quickstart on Sat Oct 20 11:30:09 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Data analysis with Python - Beta!
============================================

Note! This course instance is only for approved beta testers.

In this course an overview is given of different phases
of the data analysis pipeline using Python and its data analysis
ecosystem. What is typically done in data analysis? We assume that data is already
available, so we only need to download it. After downloading the
data it needs to be cleaned to enable further analysis. In the
cleaning phase the data is converted to some uniform and consistent
format. After which the data can be
* combined or divided into smaller chunks
* grouped or sorted,
* condensed into small number of summary statistics
* numerical or string operations can be performed on the data
The point is to manipulate the data into a form that enables discovery
of relationships and regularities among the elements of data.
Visualization of data often helps to get a better understanding of the data.
Another useful tool for data analysis is machine learning,
where a mathematical or statistical model
is fitted to the data. These models can then be used to make predictions
of new data, or can be used to explain or describe the current data.

Python is a popular, easy to learn programming language.
It is commonly used in the field of data analysis, because
there are very efficient libraries available to process large amounts of data.
This so called *data analysis stack* includes libraries such
of NumPy, Pandas, Matplotlib and SciPy that we will familiarize ourselves
with during this course.

No previous knowledge of Python is needed as will start with
a quick introduction to Python. It is however assumed that
you have good programming skills in some language.
In addition, linear algebra and probability calculus are prerequisites
of this course.
The course lasts for seven weeks and gives 5 credit units.
It is recommended that you do this course in the end of bachelor
degree or in the beginning of masters degree; preferably
before the course "Introduction to Data Analysis".

Passing the course
------------------

From the weekly programming exercises you need to get 80% of the points.
If you succeed in this, then you can start doing the project work
(approximately 1 cu of work). After the project work and
its peer reviewing is done, the you can take part in the final
exam. The final exam consists of multiple choice questions on the
themes discussed in the exercises. The final grade will be based
on the project work, its peer review, and the exam.

Note that this course requires a lot of work! Depending on your background
it can take something between 5 to 18 hours per week.
In addition to reading the course material, you sometimes may need to consult
the online documentation of Python or its various libraries.

Schedule
--------

Every week there are 15 - 20 programming exercises that you must
solve and then submit to the TMC system for checking.
In order to continue with next week's exercises you
need to get 80% of the points from exercises of the previous week.
Note that from some exercises it is possible to get more that one point.


+------+----------------+----------------------+
| Week | Deadline       | Theme                |
+======+================+======================+
| 1    | 1.1.2019 23.59 | Basics of Python I   |
+------+----------------+----------------------+
| 2    | 1.1.2019 23.59 | Basics of Python II, |
|      |                | NumPy I              |
+------+----------------+----------------------+
| 3    | 1.1.2019 23.59 | NumPy II,            |
|      |                | Visualization,       |
|      |                | Image processing,    |
|      |                | Data Analysis        |
|      |                | with Pandas I        |
+------+----------------+----------------------+
| 4    | 1.1.2019 23.59 | Data Analysis        |
|      |                | with Pandas II       |
+------+----------------+----------------------+
| 5    | 1.1.2019 23.59 | Data Analysis        |
|      |                | with Pandas III,     |
|      |                | Machine learning I   |
+------+----------------+----------------------+
| 6    | 1.1.2019 23.59 | Machine learning II, |
|      |                | Project              |
+------+----------------+----------------------+
| 7    | 1.1.2019 23.59 | Project continues    |
+------+----------------+----------------------+


Software libraries used
-----------------------

+--------------+---------------------------------------------------------+
| Library      + Documentation                                           |
+==============+=========================================================+
| numpy        | `doc <https://docs.scipy.org/doc/numpy/>`_              |
+--------------+---------------------------------------------------------+
| pandas       | `doc <http://pandas.pydata.org/pandas-docs/stable/>`_   |
+--------------+---------------------------------------------------------+
| matplotlib   | `doc <https://matplotlib.org/api/api_overview.html>`_   |
+--------------+---------------------------------------------------------+
| scikit-learn | `doc <https://scikit-learn.org/stable/>`_               |
+--------------+---------------------------------------------------------+
| scipy        | `doc <https://docs.scipy.org/doc/scipy/reference/>`_    |
+--------------+---------------------------------------------------------+





.. toctree::
   :maxdepth: 2
   :caption: Contents:

   instructions
   tools
   
.. toctree::
   :maxdepth: 2
   :caption: Week 1:

   basics

.. toctree::
   :maxdepth: 2
   :caption: Week 2:

   basics2
   numpy
   
.. toctree::
   :maxdepth: 2
   :caption: Week 3:

   numpy2	     
   matplotlib
   image_processing
   pandas1
   
.. toctree::
   :maxdepth: 2
   :caption: Week 4:

   pandas2
   
.. toctree::
   :maxdepth: 2
   :caption: Week 5:

   pandas3
   linear_regression
   
.. toctree::
   :maxdepth: 2
   :caption: Week6:

   bayes
   clustering
   pca

   
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
