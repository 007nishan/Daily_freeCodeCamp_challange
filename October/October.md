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
