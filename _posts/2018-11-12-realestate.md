---
title: 'This NY/China flat is worth HOW much?'
date: 2018-11-12
permalink: /posts/2018/11/realestate/
tags:
  - real
  - estate
  - china
  - new york
  - economics  
---
I had a cousin ask me about why Asian housing prices are so much higher than western housing prices (like in New York). Currently in my life, owning real estate does not seem so feasible, so naturally, I have no idea what these prices looked like other than being way above my pay grade. That being said, I investigated the time series prices of housing (more specifically growth of property prices) in New York vs those in China. Furthermore, the higher prices of property observed in China, also extends to Hong Kong. 

All opinions are my own and do not reflect those of the Federal Reserve Bank of New York.*

Glimpse of the Landscape
-------

I use FRED to collect the real price index of China, the US, and Hong Kong as a measure of property prices.<sup>1</sup> I also want to compare property price growth rates in China and Hong Kong to US cities that also experience this kind of growth. In this blog post, New York will be that representative city. I also use data to get the median prices of property listed on Zillow, that have been normalized to 2010 = 100. 


![fig1_ma_re](https://klai1.github.io/images/real_estate/graph_ma_real_estate.png) 

*Figure 1*: Real Estate Price Growth in US, China, Hong Kong

For starters, Figure 1 depicts the 1-year moving average growth rates of property prices in real price index in the US, China, and Hong Kong. In recent years, the real growth in the US is slightly higher than that of China’s, and Hong Kong’s real growth is higher than that of the US and China.
 
![fig2_ma_re_wNY](https://klai1.github.io/images/real_estate/graph_real_estate_wNY.png)  
 
*Figure 2*: Real Estate Price Growth in New York, China, Hong Kong

Figure 2 depicts the same analysis, but with NY instead of the US. Once again, we see similar trends as with the US.

What is striking is that even after accounting for inflation, the prices continue to grow. There has been some literature on this, especially in the case of China and Hong Kong. While Chinese and Hong Kong property prices continue to go, there has been some intervention by the Chinese Government to curb the rising real estate costs. 

The next section summarizes the existing literature to uncover why real estate prices are growing.

China and Hong Kong: What drives up the prices?
-------

It is unsurprising that property prices can grow at an increasing rate. In 2005-2006, leading up to the Great Recession, US property prices rose at an alarming rate, as many investors found it easy to invest in real estate, especially with loosened borrowing/lending restrictions. In China, property was viewed as safe investment, so when the financial markets were in bad times, much of the money flew into the housing market.

The rationale of rising property prices can be explained by fundamental economics: demand- and supply- side changes. Glaeser et. al., JEP 2017 cites these changes and also describes the differences in growth seen between the US and China. In fact, they compare the two bubbles developing in property.

**Demand Side**

Much of the Chinese (and Hong Kong) population live in cities, so higher demand for apartments or property means higher prices. While that seems to be a simple story, there are other factors driving demand:

> *Investment*

In China, many households have high saving rates, greater than those in the US. Due to the investment regulations in China (such as tight capital controls in restricting investments abroad<sup>2</sup>), these savers are being pushed to investing in real estate. Furthermore, average annual returns between 2001-2016 were zero and the average real interest rate for bank deposits has also been zero. Thus, even though mortgage rates are higher in China, Chinese investors still opt to invest money in real estate since it is much harder and not as worth it to put their money elsewhere. In Shanghai, China, real estate generates more than 10% annual real returns over the 2001-2016 period.

> *Cultural Significance - Marriage Motive*

In China (and Hong Kong), ownership of property is culturally significant, especially among newly weds and family. Upon marriage, the male side must have property in order for the female side to agree to marriage. Furthermore, families will opt to buy property for their children so the children can marry when they are of age. 

In China, home ownership is at 90% compared to that in the US, which stands at 65%. Glaesar et. al. also mention that China Household Finance Survey data points to higher levels of ownership of multiple properties and vacant properties in families with unmarried male children.  

> *Role of Government*

The Chinese government plays a huge role in restricting the investment and demand in real estate. Traditionally, this quantity restriction would cap demand at a higher price point. Sun (2017) goes into detail of all the government restrictions placed, starting with Beijing in 2010 to 18 cities in 2017.

The Chinese government monitors and intervenes in the housing market in order to maintain its stable growth. In 2010, these interventions included increasing the down-payment ratio for purchases of second homes (minimum of 40%) and increasing the profit tax rate on home resale within five years of last purchase. These measures were in place to discourage mass speculative buying of real estate (a heightened demand), as seen in the US housing bubble. Sun (2017) finds through regression discontinuity design (RDD) that housing prices dropped 17-24% after the 2010 home purchase restriction in Beijing.

Sun (2017) hypothesizes that while demand-side effects are negative, the overall effect is ambiguous because the discouragement of buying real estate might result in more available real estate, thus supply-side effects are positive. Sun focuses on Beijing housing market, so an interesting extension would be to see effects of the home purchase restrictions across more cities in China, especially with the recent expansion to 18 cities in 2017. Furthermore, we could also try to use a differences-in-differences approach to see the significance of real estate prices (or percent price changes) pre- and post-regulation.


**Supply Side**

On the supply side, I cite only one main factor that impacts the price of property:

> *Construction*

Physical cost of construction in China is low and similar across all cities. The China Engineering Cost Network report that constructions costs between $19 and $26 per square foot for building. While construction is cheaper, land is expensive and taxes are high, where Wu et. al. (2015) finds that average land price is around $3360 per square meter.

The prices of real estate in the supply side could be due to a couple factors based on construction and land costs. First, labor costs or construction quality have gone up since the 2000s, thus increasing the price of real estate. Second, the high cost of land biases the price of real estate upwards.


Conclusion
-------

In conclusion, I have cited the literature to help explain the rise (and some fall) in the prices of real estate in China. I did not dig much into Hong Kong, but the reasons are similar, but note that Hong Kong savers have more investment opportunities due to lower levels of capital controls on investment abroad (Fernandez et. al. 2015). This can be seen in comovement between growths in real estate in China and Hong Kong in Figures 1 and 2.

The demand- and supply-side arguments seem consistent with Figures 1 and 2. In China, we see dips in the growth of real estate prices around 2010, and later in around 2017, around the time of enactments of home purchase restriction policies across multiple Chinese cities. In the US, real estate plummeted between 2005 and 2008, during the time of the burst of the housing bubble and the financial crisis. Recently, housing prices in the US have stabilized to a consistent growth rate. 

Only time will tell whether the housing in China will continue growing, but my intuition is that it won’t with the home purchase restriction policies in place, especially as they are enacted in more Chinese cities.

References
-------

Fernandez, Andres, Michael Klein, Alessandro Rebucci, Martin Schindler and Martin Uribe. 2015. "Capital Control Measures: A New Dataset." *NBER Working Paper* No. 20970.

Glaeser, Edward, Wei Huang, Yueran Ma and Andrei Shleifer. 2017. "A Real Estate Boom with Chinese Characteristics." *Journal of Economic Perspectives*, 31(1): 93-116

Sun, Weizeng, Siqi Zheng, David Geltner and Rui Wang. 2016. "The Housing Market Effects of Local Home Purchase Restrictions: Evidence from Beijing." *Journal of Real Estate Finance and Economics*, 55(3): 288-312

---

<sup>* I would like to thank David Xu for his helpful comments.

<sup>1 To me, this is synonymous with Real Estate… this might not be completely correct.

<sup>2 Capital control measures found in Fernandez et. al. (2017).
