import re

pattern = re.compile(r'"createTooltipArgs"\:\s*"(.*)"')

extracted = set()

for line in open('docs/index.html'):
    matched = pattern.search(line)
    if matched:
        extracted.add(matched.group(1))

print(f'Found {len(extracted)} unique hotspot texts:')
for i, extract in enumerate(extracted):
    print(f'[{i}] {extract}')
