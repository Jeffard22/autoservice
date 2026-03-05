import os
import requests
from flask import Blueprint, render_template, request, redirect
from app.models import db, Lead

main_bp = Blueprint("main", __name__)

# ---------- UA ----------

@main_bp.route("/")
@main_bp.route("/ua")
def ua_index():
    return render_template("ua/index.html")


@main_bp.route("/ua/mobile-service")
def ua_mobile_service():
    return render_template("ua/mobile_service.html")


@main_bp.route("/ua/chiptuning")
def ua_chiptuning():
    return render_template("ua/chiptuning.html")


# ---------- EN ----------

@main_bp.route("/en")
def en_index():
    return render_template("en/index.html")


# ---------- FORM ----------

@main_bp.route("/send", methods=["POST"])
def send():
    name = request.form.get("name")
    phone = request.form.get("phone")
    message = request.form.get("message")
    page = request.referrer
    ip = request.remote_addr

    lead = Lead(
        name=name,
        phone=phone,
        message=message,
        page=page,
        ip=ip
    )
    db.session.add(lead)
    db.session.commit()

    telegram_token = os.getenv("6238440530:AAEKINIBgHtVAfGtm9TDaI9zJleb0djSCu0")
    telegram_chat_id = os.getenv("6238440530")

    text = (
        f"🚗 Нова заявка\n"
        f"Імʼя: {name}\n"
        f"Телефон: {phone}\n"
        f"Повідомлення: {message}\n"
        f"Сторінка: {page}"
    )

    requests.post(
        f"https://api.telegram.org/bot{telegram_token}/sendMessage",
        json={"chat_id": telegram_chat_id, "text": text},
        timeout=10
    )

    return redirect("/ua")
