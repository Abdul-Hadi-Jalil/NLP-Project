import 'package:flutter/material.dart';

class CardModel {
  final String title;
  final String subtitle;
  final Widget page;

  const CardModel({
    required this.title,
    required this.subtitle,
    required this.page,
  });
}
