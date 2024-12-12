from collections import deque

suggested_links = deque(map(int, input().split(' '))) #FIFO
featured_articles = list(map(int, input().split(' '))) #LIFO
target_engagement_value = int(input())

final_feed = []

while suggested_links and featured_articles:
    current_link = suggested_links.popleft()
    current_article = featured_articles.pop()

    if current_link > current_article:
        remainder = current_link % current_article
        final_feed.append(-remainder)
        if remainder == 0:
            continue
        else:
            suggested_links.append(2 * remainder)

    elif current_link < current_article:
        remainder = current_article % current_link
        final_feed.append(remainder)
        if remainder == 0:
            continue
        else:
            featured_articles.append(2 * remainder)

    elif current_link == current_article:
        final_feed.append(0)


total_engagement_value = sum(final_feed)

print(f"Final Feed: {', '.join(str(ele) for ele in final_feed)}")

if total_engagement_value >= target_engagement_value:
    print(f'Goal achieved! Engagement Value: {total_engagement_value}')
else:
    shortfall = target_engagement_value - total_engagement_value
    print(f"Goal not achieved! Short by: {shortfall}")




