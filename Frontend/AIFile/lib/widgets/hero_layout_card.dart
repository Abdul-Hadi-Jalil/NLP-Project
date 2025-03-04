import 'package:flutter/material.dart';
import '../models/card_model.dart';

class HeroLayoutCard extends StatelessWidget {
  final CardModel cardInfo;
  const HeroLayoutCard({
    super.key,
    required this.cardInfo,
  });

  @override
  Widget build(BuildContext context) {
    final double width = MediaQuery.sizeOf(context).width;
    return Stack(
        alignment: AlignmentDirectional.bottomStart,
        children: <Widget>[
          OverflowBox(
            maxWidth: width * 7 / 8,
            minWidth: width * 7 / 8,
            child: cardInfo.page,
          ),
          Padding(
            padding: const EdgeInsets.all(18.0),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              mainAxisSize: MainAxisSize.min,
              children: <Widget>[
                Text(
                  cardInfo.title,
                  overflow: TextOverflow.clip,
                  softWrap: false,
                  style: Theme.of(context)
                      .textTheme
                      .headlineLarge
                      ?.copyWith(color: Colors.white),
                ),
                const SizedBox(height: 10),
                Text(
                  cardInfo.subtitle,
                  overflow: TextOverflow.clip,
                  softWrap: false,
                  style: Theme.of(context)
                      .textTheme
                      .bodyMedium
                      ?.copyWith(color: Colors.white),
                )
              ],
            ),
          ),
        ]);
  }
}
