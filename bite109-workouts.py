workout_schedule = {'Friday': 'Shoulders',
                    'Monday': 'Chest+biceps',
                    'Saturday': 'Rest',
                    'Sunday': 'Rest',
                    'Thursday': 'Legs',
                    'Tuesday': 'Back+triceps',
                    'Wednesday': 'Core'}
rest, chill, go_train = 'Rest', 'Chill out!', 'Go train {}'


def get_workout_motd(day):
    """First title case the passed in day argument
       (so monday or MONDAY both result in Monday).

       Then check if this title cased day is in the given workout_schedule dict.

       If it is retrieve the workout (value), if not raise a KeyError.

       Return the chill variable if it's a rest day (Saturday / Sunday),
       else return the go_train variable with the workout interpolated.

       Examples:
       - if day is Saturday -> return 'Chill out!'
       - if day is Thursday -> return 'Go train Legs'
       - if day is Sunday -> return 'Chill out!'
       - if day is Monday -> return 'Go train Chest+biceps'

       Trivia: /etc/motd is a file on Unix-like systems that contains
       a 'message of the day' 


    Solution   
    try:
        workout = workout_schedule[day.title()]
    except KeyError:
        raise KeyError('Workout does not exist.')
    return chill if workout == rest else go_train.format(workout)     
        """
    
    # My code
    day = day.title()
    if day in workout_schedule:
        return chill if workout_schedule.get(day) == rest else go_train.format(workout_schedule.get(day))
    else:
        raise KeyError


