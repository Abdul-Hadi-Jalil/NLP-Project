import 'package:flutter/material.dart';
import '../data/card_data.dart';

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key});

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final PageController _pageController = PageController(initialPage: 0);

  int _currentIndex = 0;

  void _onPageChanged(int index) {
    setState(() {
      _currentIndex = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(CardData.cardList[_currentIndex].title),
      ),
      body: PageView.builder(
        controller: _pageController,
        itemCount: CardData.cardList.length,
        onPageChanged: _onPageChanged,
        itemBuilder: (context, index) {
          final card = CardData.cardList[index];
          return card.page;
        },
      ),
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _currentIndex,
        onTap: (index) {
          _pageController.animateToPage(
            index,
            duration: const Duration(milliseconds: 300),
            curve: Curves.easeInOut,
          );
        },
        items: CardData.cardList.map((card) {
          return BottomNavigationBarItem(
            icon: const Icon(Icons.circle),
            label: card.title,
          );
        }).toList(),
      ),
    );
  }
}
