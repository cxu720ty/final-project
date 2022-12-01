#!/usr/bin/env python
# coding: utf-8

# ## Results
# It seems that the **Wolfgang Reitherman** is very productive

# ![result](../result.png)

# Now it's time to answer the original question. Which directors have the most inflation gross of average of each movie? To do this, I will make a new dataframe by merging **avg_inflation_gross_by_director** and **movie_count**

# director_count_gross = avg_inflation_gross_by_director.merge(movie_count, left_on='director', right_on='director', how='left', indicator=True)
# director_count_gross  =director_count_gross.assign(director_avg_gross_per_movie=director_count_gross['inflation_adjusted_gross'] *director_count_gross['count'])
# director_count_gross
# 
# #director_count_gross_max = director_count_gross['director_avg_gross_per_movie'].max()
# director_count_gross_max=director_count_gross.loc[director_count_gross['director_avg_gross_per_movie'] == director_count_gross['director_avg_gross_per_movie'].max()]
# director_count_gross_max

# It seems that in fact it is **Davied Hand** has max average inflation gross per movie. 

# In[1]:


we can take a look at the chart of each director's inflation gross. 


# In[ ]:


# Visualize the top 20 themes with the most sets using a bar plot.
director_count_gross_plot = (
    alt.Chart(director_count_gross, width=500, height=300)
    .mark_bar()
    .encode(
        x=alt.X("director:N", title="Directors", sort="-y"),
        y=alt.Y("director_avg_gross_per_movie:Q", title="Inflation per Movie"),
    )
    .properties(title="Director Average per Movie (Adjusted for Inflation)")
)
director_count_gross_plot


# ![Disneyland](../disney2.png)

# In[ ]:




