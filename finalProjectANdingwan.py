#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 23:04:21 2020

@author: yannique
"""

data = "Documents/Data/FullData.csv"


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# % matplotlib inline


df = pd.read_csv("FullData.csv")
df.head(10)



del df['National_Kit'] #deletes the column National_Kit
df.head()

#This graph gives us the number of players representing a particular country. 
#Now, these graphs are best used to gain statistical insights.
plt.figure(figsize=(15,32))
sns.countplot(y = df.Nationality,palette="Set2") #Plot all the nations on Y Axis


#Using this graph, we conclude that most of the players are from England, Argentina, Spain, France and Brazil. 
#In this case, the graph won’t add a lot of value because we would be picking the best XI, and the results may vary.

plt.figure(figsize=(15,6))
sns.countplot(x="Age",data=df)

#It is evident from the above screenshot that the majority of players are between the age of 20 and 29,
# with the largest peak of 25 years.

#World’s Best Playing XI: Finding The Best Goalkeeper
#Shot Stopper: A goalkeeper who is strong in stopping shots taken by opponents.
#Sweeper: A goalkeeper who is strong in playing with his feet and making passes.

#weights
a = 0.5
b = 1
c= 2
d = 3
 
#GoalKeeping Characterstics
df['gk_Shot_Stopper'] = (b*df.Reactions + b*df.Composure + a*df.Speed + a*df.Strength + c*df.Jumping + b*df.GK_Positioning + c*df.GK_Diving + d*df.GK_Reflexes + b*df.GK_Handling)/(2*a + 4*b + 2*c + 1*d)
df['gk_Sweeper'] = (b*df.Reactions + b*df.Composure + b*df.Speed + a*df.Short_Pass + a*df.Long_Pass + b*df.Jumping + b*df.GK_Positioning + b*df.GK_Diving + d*df.GK_Reflexes + b*df.GK_Handling + d*df.GK_Kicking + c*df.Vision)/(2*a + 4*b + 3*c + 2*d)


#Based on the above parameters, I’ll be predicting my best goalkeeper as per the dataset. Let us now plot these parameters:

plt.figure(figsize=(15,6))
 
# Generate sequential data and plot
sd = df.sort_values('gk_Shot_Stopper', ascending=False)[:5]
x1 = np.array(list(sd['Name']))
y1 = np.array(list(sd['gk_Shot_Stopper']))
sns.barplot(x1, y1, palette= "colorblind")
plt.ylabel("Shot Stopping Score")




#Based on the shot-stopper characteristics, 
#it can be inferred that Manuel Neuer is the best goalkeeper as you can see he tops the above list. Let us now plot the other parameter(Sweeper) as well.

plt.figure(figsize=(15,6))
sd = df.sort_values('gk_Sweeper', ascending=False)[:5]
x2 = np.array(list(sd['Name']))
y2 = np.array(list(sd['gk_Sweeper']))
sns.barplot(x2, y2, palette= "colorblind")
plt.ylabel("Sweeping Score")

#Manuel Neuer tops the chart here as well. Based on the two parameters we used, 
#we can conclude that Manuel Neuer would be the best choice goalkeeper for the World Cup 2018.


#In order to find the best defenders, I’ll be using following attributes to fetch the best defenders:
#Centre Backs: We need two center-backs. One who plays LCB and the other who plays RCB.
#Wing Backs: We again need two wing backs. One who plays on the Left and the other who plays on the right.


#Choosing Defenders
df['df_centre_backs'] = ( d*df.Reactions + c*df.Interceptions + d*df.Sliding_Tackle + d*df.Standing_Tackle + b*df.Vision+ b*df.Composure + b*df.Crossing +a*df.Short_Pass + b*df.Long_Pass+ c*df.Acceleration + b*df.Speed
+ d*df.Stamina + d*df.Jumping + d*df.Heading + b*df.Long_Shots + d*df.Marking + c*df.Aggression)/(6*b + 3*c + 7*d)
df['df_wb_Wing_Backs'] = (b*df.Ball_Control + a*df.Dribbling + a*df.Marking + d*df.Sliding_Tackle + d*df.Standing_Tackle + a*df.Attacking_Position + c*df.Vision + c*df.Crossing + b*df.Short_Pass + c*df.Long_Pass + d*df.Acceleration +d*df.Speed + c*df.Stamina + a*df.Finishing)/(4*a + 2*b + 4*c + 4*d)


#LEFT CENTRAL DEFENDER:

plt.figure(figsize=(15,6))
sd = df[(df['Club_Position'] == 'LCB')].sort_values('df_centre_backs', ascending=False)[:5]
x2 = np.array(list(sd['Name']))
y2 = np.array(list(sd['df_centre_backs']))
sns.barplot(x2, y2, palette=sns.color_palette("Blues_d"))
plt.ylabel("LCB Score")


#RIGHT CENTRAL DEFENDER:
plt.figure(figsize=(15,6))
sd = df[(df['Club_Position'] == 'RCB')].sort_values('df_centre_backs', ascending=False)[:5]
x2 = np.array(list(sd['Name']))
y2 = np.array(list(sd['df_centre_backs']))
sns.barplot(x2, y2, palette=sns.color_palette("Blues_d"))
plt.ylabel("RCB Score")


#Based on the right centre back characteristics, it can be inferred that Azpilicueta is the Best Right Central Defender.
#Based on the left centre back characteristics, it can be inferred that Sergio Ramos is the Best Left Central Defender. Let us now plot the RCB as well.


#LEFT WING BACK:

plt.figure(figsize=(15,6))
 
sd = df[(df['Club_Position'] == 'LWB') | (df['Club_Position'] == 'LB')].sort_values('df_wb_Wing_Backs', ascending=False)[:5]
x4 = np.array(list(sd['Name']))
y4 = np.array(list(sd['df_wb_Wing_Backs']))
sns.barplot(x4, y4, palette=sns.color_palette("Blues_d"))
plt.ylabel("Left Back Score")


#Since David Alaba’s team does not qualify in the world cup 2018, I’ll be picking Alex Sandro as the best LWB/LB defender.


#RIGHT WING BACK:
plt.figure(figsize=(15,6))
sd = df[(df['Club_Position'] == 'RWB') | (df['Club_Position'] == 'RB')].sort_values('df_wb_Wing_Backs', ascending=False)[:5]
x5 = np.array(list(sd['Name']))
y5 = np.array(list(sd['df_wb_Wing_Backs']))
sns.barplot(x5, y5, palette=sns.color_palette("Blues_d"))
plt.ylabel("Right Back Score")

#As per the above analysis, it is evident that Kyle Walker is the best RWB/RB for World Cup 2018.
#Having said that, below is the list of the best defenders for this World Cup 2018:


#I have to choose 3 midfielders. In order to find these, I’ll be analyzing the data for the below mentioned parameters:
#Playmaker: A playmaker is someone who will move the ball to the attacking 3rd from defence or midfield.
#Beast:A beast is a typical box-to-box player with loads of energy and who can boss the midfield.
#Controller:A controller is the person who is orchestrating your midfield engine by either sitting back or going forward based on dynamic needs.

#Midfielding Indices
df['mf_playmaker'] = (d*df.Ball_Control + d*df.Dribbling + a*df.Marking + d*df.Reactions + d*df.Vision + c*df.Attacking_Position + c*df.Crossing + d*df.Short_Pass + c*df.Long_Pass + c*df.Curve + b*df.Long_Shots + c*df.Freekick_Accuracy)/(1*a + 1*b + 4*c + 4*d)
df['mf_beast'] = (d*df.Agility + c*df.Balance + b*df.Jumping + c*df.Strength + d*df.Stamina + a*df.Speed + c*df.Acceleration + d*df.Short_Pass + c*df.Aggression + d*df.Reactions + b*df.Marking + b*df.Standing_Tackle + b*df.Sliding_Tackle + b*df.Interceptions)/(1*a + 5*b + 4*c + 4*d)
df['mf_controller'] = (b*df.Weak_foot + d*df.Ball_Control + a*df.Dribbling + a*df.Marking + a*df.Reactions + c*df.Vision + c*df.Composure + d*df.Short_Pass + d*df.Long_Pass)/(2*c + 3*d + 4*a)


#PLAYMAKER
plt.figure(figsize=(15,6))
 
ss = df[(df['Club_Position'] == 'CAM') | (df['Club_Position'] == 'LAM') | (df['Club_Position'] == 'RAM')].sort_values('mf_playmaker', ascending=False)[:5]
x3 = np.array(list(ss['Name']))
y3 = np.array(list(ss['mf_playmaker']))
sns.barplot(x3, y3, palette=sns.diverging_palette(145, 280, s=85, l=25, n=5))
plt.ylabel("PlayMaker Score")

#I’ll pick Mesut Ozil as the best Playmaker for World Cup 2018.


#PLAYMAKER:
plt.figure(figsize=(15,6))
 
ss = df[(df['Club_Position'] == 'RCM') | (df['Club_Position'] == 'RM')].sort_values('mf_beast', ascending=False)[:5]
x2 = np.array(list(ss['Name']))
y2 = np.array(list(ss['mf_beast']))
sns.barplot(x2, y2, palette=sns.diverging_palette(145, 280, s=85, l=25, n=5))
plt.ylabel("Beast Score")

#N’ Golo Kante as the best Beast/ Right Central Midfielder.

#Controller:
plt.figure(figsize=(10,6))
 
# Generate some sequential data
ss = df[(df['Club_Position'] == 'LCM') | (df['Club_Position'] == 'LM')].sort_values('mf_controller', ascending=False)[:5]
x1 = np.array(list(ss['Name']))
y1 = np.array(list(ss['mf_controller']))
sns.barplot(x1, y1, palette=sns.diverging_palette(145, 280, s=85, l=25, n=5))
plt.ylabel("Controller Score")


#In order to find the best attacker, I’ll be analyzing the below mentioned parameters:
#Attacking Left Wing: He is a player, attacking from the left flank.
#Attacking Right Wing: He is a player, attacking from the right flank.
#Striker: He is a player attacking from the center.

#Attackers
df['att_left_wing'] = (c*df.Weak_foot + c*df.Ball_Control + c*df.Dribbling + c*df.Speed + d*df.Acceleration + b*df.Vision + c*df.Crossing + b*df.Short_Pass + b*df.Long_Pass + b*df.Aggression + b*df.Agility + a*df.Curve + c*df.Long_Shots + b*df.Freekick_Accuracy + d*df.Finishing)/(a + 6*b + 6*c + 2*d)
df['att_right_wing'] = (c*df.Weak_foot + c*df.Ball_Control + c*df.Dribbling + c*df.Speed + d*df.Acceleration + b*df.Vision + c*df.Crossing + b*df.Short_Pass + b*df.Long_Pass + b*df.Aggression + b*df.Agility + a*df.Curve + c*df.Long_Shots + b*df.Freekick_Accuracy + d*df.Finishing)/(a + 6*b + 6*c + 2*d)
df['att_striker'] = (b*df.Weak_foot + b*df.Ball_Control + a*df.Vision + b*df.Aggression + b*df.Agility + a*df.Curve + a*df.Long_Shots + d*df.Balance + d*df.Finishing + d*df.Heading + c*df.Jumping + c*df.Dribbling)/(3*a + 4*b + 2*c + 3*d)


#Left wing attacker.
plt.figure(figsize=(15,6))
ss = df[(df['Club_Position'] == 'LW') | (df['Club_Position'] == 'LM') | (df['Club_Position'] == 'LS')].sort_values('att_left_wing', ascending=False)[:5]
x1 = np.array(list(ss['Name']))
y1 = np.array(list(ss['att_left_wing']))
sns.barplot(x1, y1, palette=sns.diverging_palette(255, 133, l=60, n=5, center="dark"))
plt.ylabel("Left Wing")
#It’s quite evident from the above plot that Ronaldo is the best Left Wing Attacker 


#right wing attacker.
ss = df[(df['Club_Position'] == 'RW') | (df['Club_Position'] == 'RM') | (df['Club_Position'] == 'RS')].sort_values('att_right_wing', ascending=False)[:5]
x2 = np.array(list(ss['Name']))
y2 = np.array(list(ss['att_right_wing']))
sns.barplot(x2, y2, palette=sns.diverging_palette(255, 133, l=60, n=5, center="dark"))
plt.ylabel("Right Wing")
#Lionel Messi as the right wing attacker for World Cup 2018.


#STRIKER
plt.figure(figsize=(15,6))
ss = df[(df['Club_Position'] == 'ST') | (df['Club_Position'] == 'LS') | (df['Club_Position'] == 'RS') | (df['Club_Position'] == 'CF')].sort_values('att_striker', ascending=False)[:5]
x3 = np.array(list(ss['Name']))
y3 = np.array(list(ss['att_striker']))
sns.barplot(x3, y3, palette=sns.diverging_palette(255, 133, l=60, n=5, center="dark"))
plt.ylabel("Striker")



