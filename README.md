# multimedia
### This is the repo for developing the algorithm for MediaEval 2018 Task

#### Task Description:
Affective video content analysis aims at the automatic recognition of emotions elicited by videos. 
It has a large number of applications, including emotion-based personalized content delivery, video indexing, summarization and protection of children from potentially harmful video content. While major progress has been achieved in computer vision for visual object detection, scene understanding and high-level concept recognition, a natural further step is the modeling and recognition of affective concepts. This has recently received increasing interest from research communities, e.g., computer vision, machine learning, with an overall goal of endowing computers with human-like perception capabilities. Thus, this task is proposed to offer researchers a place to compare their approaches for the prediction of the emotional impact of movies. It is a sequel of last year’s task.

1. Valence/Arousal prediction: predict a score of induced valence (negative-positive) and induced arousal (calm-excited) continuously (every second) along movies;
2. Fear prediction: predict beginning and ending times of sequences inducing fear in movies. 
The targeted use case is the prediction of frightening scenes to help systems protecting children from potentially harmful video content.

#### Integrate temporal information into models. As the emotion felt while watching a movie scene depend not only on the current scene but also on previous scenes and previous felt emotions, a temporal modeling is useful. ex: Long Short-Term Memory or temporal smoothing to the predicted values.
