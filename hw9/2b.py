class Activity:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return "start:{} end:{}".format(self.start, self.end)

    def overlaps(self, other):
        # check if two activities overlaps
        if not (self.start >= other.end or self.end <= other.start):
            print("overlaps: first - {} second - {}".format(self, other))
            return True
        else:
            return False

def hasConflict(selected, current):
    # check if it has any collision in the list
    for s in selected:
        if s.overlaps(current):
            return True
    return False

def selectActivity(activities, selectedList = []):
    # base case
    if activities == []:
        return 0

    # break the list into head, which is called current
    # and tail, which is called remaining
    current, *remaining = activities

    if hasConflict(selectedList, current):
        return selectActivity(remaining, selectedList)
    else:
        # either you include the head or not
        included = 1 + selectActivity(remaining, selectedList + [current])
        excluded = selectActivity(remaining, selectedList)

        # find the biggest one
        if included > excluded:
            return included
        return excluded

def includeLastSelection(activities):
    # force inclusion of the last activity
    return 1 + selectActivity(activities[:-1], activities[-1:])
