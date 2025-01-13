import '../models/card_model.dart';
import '../views/download_file_page.dart';
import '../views/perform_action_page.dart';
import '../views/select_file_page.dart';

class CardData {
  static const List<CardModel> cardList = <CardModel>[
    CardModel(
      title: 'Select File',
      subtitle: 'Upload the file you want to perform action on',
      page: SelectFilePage(),
    ),
    CardModel(
      title: 'Select The option',
      subtitle: 'Select the action you want to perform on the file',
      page: PerformActionPage(),
    ),
    CardModel(
      title: 'Download File',
      subtitle: 'Download the file after the action is performed',
      page: DownloadFilePage(),
    ),
  ];
}
