#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telebot
from bs4 import BeautifulSoup
import requests
from telebot import types
import os
import sys

#headers нужен,что бы сайт не понял,что парсит бот
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}

bot = telebot.TeleBot('1149414374:AAFvUi0Z_O25o3tlGSrDa8BVjf6eiAlSMnc')

# Стандартый обработчик команды старт
@bot.message_handler(commands=['start'])
def main(message):
	
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
	btn1 = types.KeyboardButton('Курс валют')
	markup.row(btn1)
	bot.send_message(message.chat.id, "Выбери нужное действие:",reply_markup=markup)

@bot.message_handler(content_types=['text'])
def kurs(message):
	if message.text == "Курс валют":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('Моно-Сбер')
		btn2 = types.KeyboardButton('Моно-Киви')
		btn3 = types.KeyboardButton('Назад')
		markup.row(btn1, btn2)
		markup.add(btn3)
		final_message = "Выбери пару"
		

	elif message.text == "Моно-Сбер":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('Моно-Сбер')
		btn2 = types.KeyboardButton('Моно-Киви')
		btn3 = types.KeyboardButton('Назад')
		markup.row(btn1, btn2)
		markup.add(btn3)
		MONO_SBER = 'https://mine.exchange/exchange_MONOBUAH_to_SBERRUB'
		full_page = requests.get(MONO_SBER, headers=headers)
		soup = BeautifulSoup(full_page.content, 'html.parser')
		convert = soup.findAll("input", {"type": "text", "class": "js_summ2"})
		print("Сейчас курс: 1 Грн = " + convert[0]['value'],"руб")
		resul = convert[0]['value']				
		final_message = "Сейчас курс: 1 Грн = " + resul + " руб"
	
		


	elif message.text == "Моно-Киви":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('Моно-Сбер')
		btn2 = types.KeyboardButton('Моно-Киви')
		btn3 = types.KeyboardButton('Назад')
		markup.row(btn1, btn2)
		markup.add(btn3)
		MONO_QIWI = 'https://mine.exchange/exchange_MONOBUAH_to_QWRUB/'
		full_page = requests.get(MONO_QIWI, headers=headers)
		soup = BeautifulSoup(full_page.content, 'html.parser')
		convert = soup.findAll("input", {"type": "text", "class": "js_summ2"})
		print("Сейчас курс: 1 Грн = " + convert[0]['value'],"QIWI руб")
		resul = convert[0]['value']				
		final_message = "Сейчас курс: 1 Грн = " + resul + " QIWI руб"
		
		


	elif message.text == "Назад":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('Курс валют')
		markup.row(btn1)
		final_message = "Главное меню"
		

	else:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

		final_message = "Нажимай то,что предлагают, а не сам придумывай!"
		




	bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)
	



if __name__ == '__main__':
	executor.start_polling(dp)
    