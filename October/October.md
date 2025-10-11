<h1>Space Week</h1>
<p>October 4<sup>th</sup> marks the beginning of <strong>World Space Week</strong>. The next seven days will bring you astronomy-themed coding challenges.</p>
<h2>Day 1: Stellar Classification</h2>
<h3>4<sup>th</sup> October</h3>
For today's challenge, you are given the surface temperature of a star in Kelvin (K) and need to determine its stellar classification based on the following ranges:</br>
<ul>
  <li><code>"O"</code>: 30,000 K or higher</li>
  <li><code>"B"</code>: 10,000 K - 29,999 K</li>
  <li><code>"A"</code>: 7,500 K - 9,999 K</li>
  <li><code>"F"</code>: 6,000 K - 7,499 K</li>
  <li><code>"G"</code>: 5,200 K - 5,999 K</li>
  <li><code>"K"</code>: 3,700 K - 5,199 K</li>
  <li><code>"M"</code>: 0 K - 3,699 K</li>
  <li>Return the classification of the given star.</li>
</ul>
<h2>Day 2: Exoplanet Search</h2>
<h3>5<sup>th</sup> October</h3>
<p>For the second day of Space Week, you are given a string where each character represents the luminosity reading of a star. Determine if the readings have detected an exoplanet using the transit method. The transit method is when a planet passes in front of a star, reducing its observed luminosity.</p>
<ul>
  <li>Luminosity readings only comprise of characters <code>0-9</code> and <code>A-Z</code> where each reading corresponds to the following numerical values:</li>
  <ul>
    <li>Characters <code>0-9</code> correspond to luminosity levels <code>0-9</code>.</li>
    <li>Characters <code>A-Z</code> correspond to luminosity levels <code>10-35</code>.</li>
  </ul>
</ul>
<p>A star is considered to have an exoplanet if any single reading is less than or equal to 80% of the average of all readings. For example, if the average luminosity of a star is 10, it would be considered to have a exoplanet if any single reading is 8 or less.</p>
<h2>Day 3: Phone Home</h2>
<h3>6<sup>th</sup> October</h3>
<p>For day three of Space Week, you are given an array of numbers representing distances (in kilometers) between yourself, satellites, and your home planet in a communication route. Determine how long it will take a message sent through the route to reach its destination planet using the following constraints:</p>
<ul>
  <li>The first value in the array is the distance from your location to the first satellite.</li>
  <li>Each subsequent value, except for the last, is the distance to the next satellite.</li>
  <li>The last value in the array is the distance from the previous satellite to your home planet.</li>
  <li>The message travels at 300,000 km/s.</li>
  <li>Each satellite the message passes through adds a 0.5 second transmission delay.</li>
  <li>Return a number rounded to 4 decimal places, with trailing zeros removed.</li>
</ul>

<h2>Day 4: Landing Spot</h2>
<h3>7<sup>th</sup> October, 2025</h3>
<p>In day four of Space Week, you are given a matrix of numbers (an array of arrays), representing potential landing spots for your rover. Find the safest landing spot based on the following rules:</p>
<ul>
  <li>Each spot in the matrix will contain a number from <code>0-9</code>, inclusive.</li>
  <li>Any <code>0</code> represents a potential landing spot.</li>
  <li>Any number other than <code>0</code> is too dangerous to land. The higher the number, the more dangerous.</li>
  <li>The safest spot is defined as the <code>0</code> cell whose surrounding cells (up to 4 neighbors, ignore diagonals) have the lowest total danger.</li>
  <li>Ignore out-of-bounds neighbors (corners and edges just have fewer neighbors).</li>
  <li>Return the indices of the safest landing spot. There will always only be one safest spot.</li>
</ul>
<p>For instance, given:</br>
<pre class="code-box">
[
  [1, 0],
  [2, 0]
]
</pre>

Return <code>[0, 1]</code>, the indices for the <code>0</code> in the first array.</p>

<h2>Day 5: Goldilocks Zone</h2>
<h3>8<sup>th</sup> October, 2025</h3>
<p>For the fifth day of Space Week, you will calculate the "Goldilocks zone" of a star - the region around a star where conditions are "just right" for liquid water to exist.</p>
<p>Given the mass of a star, return an array with the start and end distances of its Goldilocks Zone in Astronomical Units.</p>
<p>To calculate the Goldilocks Zone:</p>
<ol>
  <li>Find the luminosity of the star by raising its mass to the power of 3.5.</li>
  <li>The start of the zone is 0.95 times the square root of its luminosity.</li>
  <li>The end of the zone is 1.37 times the square root of its luminosity.</li>
</ol>
<ul>
  <li>Return the distances rounded to two decimal places.</li>
</ul>
<p>For example, given <code>1</code> as a mass, return <code>[0.95, 1.37]</code>.</p>
