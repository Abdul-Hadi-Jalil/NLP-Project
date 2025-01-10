import 'package:ai_file/models/card_model.dart';
import 'package:flutter/material.dart';
import '../constants/constants.dart';
import '../data/card_data.dart';
import '../widgets/hero_layout_card.dart';

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key});

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final CarouselController controller = CarouselController(initialItem: 0);
  @override
  Widget build(BuildContext context) {
    final double height = MediaQuery.sizeOf(context).height;
    return Scaffold(
      appBar: AppBar(
        title: const Text(AppText.appName),
      ),
      body: ConstrainedBox(
        constraints: BoxConstraints(maxHeight: height),
        child: CarouselView.weighted(
          controller: controller,
          itemSnapping: true,
          flexWeights: const <int>[1, 7, 1],
          children: CardData.cardList.map((CardModel card) {
            return HeroLayoutCard(cardInfo: card);
          }).toList(),
        ),
      ),
    );
  }

  @override
  void dispose() {
    controller.dispose();
    super.dispose();
  }
}
