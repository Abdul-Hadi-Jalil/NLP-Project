import 'package:flutter/material.dart';

class PerformActionPage extends StatelessWidget {
  const PerformActionPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Perform Action'),
      ),
      body: Container(
        color: Colors.cyanAccent,
        child: Center(
          child: Container(
            width: 200,
            padding: EdgeInsets.all(20),
            decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(10),
            ),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                InkWell(
                  onTap: () {},
                  child: Text('Convert to xlsx'),
                ),
                Divider(
                  color: Colors.black,
                  thickness: 1,
                ),
                InkWell(
                  onTap: () {},
                  child: Text('Document summary'),
                ),
                Divider(
                  color: Colors.black,
                  thickness: 1,
                ),
                InkWell(
                  onTap: () {},
                  child: Text('Language Translation'),
                ),
                Divider(
                  color: Colors.black,
                  thickness: 1,
                ),
                InkWell(
                  onTap: () {},
                  child: Text('Language detection'),
                ),
                Divider(
                  color: Colors.black,
                  thickness: 1,
                ),
                InkWell(
                  onTap: () {},
                  child: Text('Sentiment analysis'),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
